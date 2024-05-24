{ pkgs }: {
  deps = [
    pkgs.python311Packages.wagtail
    pkgs.python-launcher
    pkgs.wget
    pkgs.docker-client
    pkgs.docker
  ];
}