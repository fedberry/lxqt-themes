Name:           lxqt-themes
Version:        0.13.0
Release:        3%{?dist}
Summary:        LXQt standard themes

License:        LGPLv2+
URL:            https://lxqt.org/
Source0:        https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(lxqt)

Requires:       hicolor-icon-theme
Requires:       fedora-logos
Requires:       desktop-backgrounds-compat
Requires:       oxygen-cursor-themes
Requires:       oxygen-icon-theme

# The themes were essential part of the previous lxqt-common package which
# no longer exists. Therefore we obsolete and provide it here:
Provides:       lxqt-common = %{version}-%{release}
Obsoletes:      lxqt-common < 0.12.0
# The old name for the theme subpackage was lxqt-theme
Provides:       lxqt-theme = %{version}-%{release}
Obsoletes:      lxqt-theme < 0.12.0

%description
This package contains the standard themes for the LXQt desktop, namely
ambiance, dark, frost, kde-plasma, light and system.

%prep
%autosetup


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
#    %%{cmake_lxqt} -DPULL_TRANSLATIONS=NO ..
     %{cmake} ..
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_datadir}/lxqt/{graphics,themes}
%{_datadir}/icons/hicolor/scalable/*/*.svg


%changelog
* Fri Aug 24 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-3
- Bump for package review

* Sun Jun 03 2018 Christian Dersch <lupinix@mailbox.org> - 0.13.0-2
- add requirements for the themes

* Sun Jun  3 2018 Christian Dersch <lupinix@mailbox.org> - 0.13.0-1
- initial package

