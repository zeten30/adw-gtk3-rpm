Name:           adw-gtk3
Version:        1.7
Release:        2%{?dist}
Summary:        The theme from libadwaita ported to GTK-3
License:        GPLv2+
URL:            https://github.com/lassekongo83/adw-gtk3
BuildRequires: sassc
BuildRequires: git
BuildRequires: meson
BuildRequires: ninja-build

%description
The theme from libadwaita ported to GTK-3


%prep
git clone --recurse-submodules https://github.com/lassekongo83/adw-gtk3.git

%build
cd adw-gtk3
git checkout tags/v1.7
%meson
%meson_build

%install
cd adw-gtk3
%meson_install

%files
%{_datadir}/themes/adw-gtk3/*
%{_datadir}/themes/adw-gtk3-dark/*
