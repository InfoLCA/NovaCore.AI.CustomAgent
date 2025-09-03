{
  description = "NovaCore dev shell";
  inputs = { nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable"; };
  outputs = { self, nixpkgs }:
  let
    system = "aarch64-darwin";
    pkgs = import nixpkgs { inherit system; };
  in {
    devShells.${system}.default = pkgs.mkShell {
      packages = with pkgs; [ python311 python311Packages.pip python311Packages.virtualenv git jq yq ];
      shellHook = ''echo "[nix] NovaCore dev shell ready"'';
    };
  };
}
