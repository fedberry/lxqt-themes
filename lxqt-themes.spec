Name:           lxqt-themes
Version:        0.13.0
Release:        6%{?dist}
Summary:        LXQt standard themes

License:        LGPLv2+
URL:            https://lxqt.org/
Source0:        https://downloads.lxqt.org/downloads/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        lxqt-themes-fedberry.tar.xz
BuildArch:      noarch

BuildRequires:  lxqt-build-tools
BuildRequires:  pkgconfig(lxqt)

Requires:       hicolor-icon-theme
Requires:       desktop-backgrounds-compat
Requires:       breeze-cursor-themes
Requires:       breeze-icon-theme

Provides:       lxqt-common = %{version}-%{release}
Provides:       lxqt-theme = %{version}-%{release}

Obsoletes:      lxqt-common < 0.12.0
Obsoletes:      lxqt-theme < 0.12.0


%description
This package contains the standard themes for the LXQt desktop, namely
ambiance, dark, frost, kde-plasma, light and system.


%package fedberry
Summary: Default Fedberry theme for LXQt
Requires: lxqt-theme = %{version}
Requires: breeze-cursor-theme
Requires: breeze-icon-theme
Requires: plasma-breeze
Requires: fedberry-logos

Provides:       lxqt-theme-fedberry = %{version}-%{release}
Obsoletes:      lxqt-theme-fedberry < %{version}-%{release}


%description fedberry
%{summary}.


%prep
%autosetup
%setup -b 1


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
     %{cmake} ..
popd
make %{?_smp_mflags} -C %{_target_platform}


# Build Fedberry theme
pushd %{_builddir}/lxqt-themes-fedberry
tar Jxf %{SOURCE1}
mkdir -p %{_target_platform}
pushd %{_target_platform}
     %{cmake} ..
popd
popd


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# Install Fedberry theme
pushd %{_builddir}/lxqt-themes-fedberry
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
popd
exit


%files
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_datadir}/lxqt/graphics
%dir %{_datadir}/lxqt/themes
%{_datadir}/lxqt/themes/{ambiance,dark,frost,kde-plasma,light,system}
%{_datadir}/icons/hicolor/scalable/*/*.svg


%files fedberry
%{_datadir}/lxqt/themes/fedberry


%changelog
* Thu Nov 15 2018 Vaughan <devel at agrez.net> - 0.13.0-6
- Import into Fedberry (Thanks Fedora)
- Add fedberry theme from depreciated lxqt-common pkg
- Bump release

* Mon Sep 03 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-5
- Obsolete and provide the old subpackage of lxqt-common
- Fixes RHBZ 1624739

* Sun Aug 26 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-4
- Merge lxqt-themes-fedora into lxqt-themes

* Fri Aug 24 2018 Zamir SUN <zsun@fedoraproject.org> - 0.13.0-3
- Bump for package review

* Sun Jun 03 2018 Christian Dersch <lupinix@mailbox.org> - 0.13.0-2
- add requirements for the themes

* Sun Jun  3 2018 Christian Dersch <lupinix@mailbox.org> - 0.13.0-1
- initial package

