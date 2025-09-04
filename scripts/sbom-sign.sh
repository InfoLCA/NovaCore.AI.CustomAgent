#!/usr/bin/env bash
set -euo pipefail

SBOM="security/sboms/syft_sbom.json"
SIG="security/attestations/cosign_signatures/syft_sbom.sig"

mkdir -p "$(dirname "$SBOM")" "$(dirname "$SIG")"

need() { command -v "$1" >/dev/null 2>&1 || { echo "Missing $1. Install it (e.g., brew install $1)"; exit 127; }; }

need syft
need cosign

echo "Generating CycloneDX SBOM with syft → $SBOM"
syft . -o cyclonedx-json > "$SBOM"

echo "Keyless-signing SBOM with Cosign → $SIG"
export COSIGN_EXPERIMENTAL=1
cosign sign-blob --yes --output-signature "$SIG" "$SBOM"

echo "Done."
echo "SBOM:       $SBOM"
echo "Signature:  $SIG"
