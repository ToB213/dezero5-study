{
  description = "dezero5-study dev shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }:
    let
      system = "aarch64-darwin";
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShells.${system}.default = pkgs.mkShell {
        buildInputs = [
          pkgs.python311
          pkgs.zlib
          pkgs.openssl
        ];

        shellHook = ''
          if [ ! -d .venv ]; then
            python -m venv .venv
          fi
          source .venv/bin/activate
        '';
      };
    };
}