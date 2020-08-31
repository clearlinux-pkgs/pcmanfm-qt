#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : pcmanfm-qt
Version  : 0.15.1
Release  : 5
URL      : https://github.com/lxqt/pcmanfm-qt/releases/download/0.15.1/pcmanfm-qt-0.15.1.tar.xz
Source0  : https://github.com/lxqt/pcmanfm-qt/releases/download/0.15.1/pcmanfm-qt-0.15.1.tar.xz
Source1  : https://github.com/lxqt/pcmanfm-qt/releases/download/0.15.1/pcmanfm-qt-0.15.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: pcmanfm-qt-bin = %{version}-%{release}
Requires: pcmanfm-qt-data = %{version}-%{release}
Requires: pcmanfm-qt-license = %{version}-%{release}
Requires: pcmanfm-qt-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : doxygen
BuildRequires : libexif-dev
BuildRequires : libfm-qt-dev
BuildRequires : liblxqt-data
BuildRequires : lxqt-build-tools
BuildRequires : menu-cache-dev
BuildRequires : qtbase-dev
BuildRequires : qttools-dev
BuildRequires : qtx11extras-dev

%description
# PCManFM-Qt
## Overview
PCManFM-Qt is the Qt port of PCManFM, the file manager of [LXDE](https://lxde.org).

%package bin
Summary: bin components for the pcmanfm-qt package.
Group: Binaries
Requires: pcmanfm-qt-data = %{version}-%{release}
Requires: pcmanfm-qt-license = %{version}-%{release}

%description bin
bin components for the pcmanfm-qt package.


%package data
Summary: data components for the pcmanfm-qt package.
Group: Data

%description data
data components for the pcmanfm-qt package.


%package license
Summary: license components for the pcmanfm-qt package.
Group: Default

%description license
license components for the pcmanfm-qt package.


%package man
Summary: man components for the pcmanfm-qt package.
Group: Default

%description man
man components for the pcmanfm-qt package.


%prep
%setup -q -n pcmanfm-qt-0.15.1
cd %{_builddir}/pcmanfm-qt-0.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598900562
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1598900562
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pcmanfm-qt
cp %{_builddir}/pcmanfm-qt-0.15.1/LICENSE %{buildroot}/usr/share/package-licenses/pcmanfm-qt/db95910cb27890d60e596e4c622fc3eeba6693fa
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcmanfm-qt

%files data
%defattr(-,root,root,-)
/usr/share/applications/pcmanfm-qt-desktop-pref.desktop
/usr/share/applications/pcmanfm-qt.desktop
/usr/share/pcmanfm-qt/lxqt/settings.conf
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_ar.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_arn.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_ast.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_ca.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_cs.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_cy.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_da.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_de.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_el.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_en_GB.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_es.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_et.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_fil.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_fr.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_gl.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_he.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_hi.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_hu.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_id.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_it.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_ja.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_lt.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_nb_NO.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_nl.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_pl.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_pt.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_pt_BR.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_pt_PT.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_ru.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_sk_SK.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_sv.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_tr.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_uk.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_zh_CN.qm
/usr/share/pcmanfm-qt/translations/pcmanfm-qt_zh_TW.qm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pcmanfm-qt/db95910cb27890d60e596e4c622fc3eeba6693fa

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/pcmanfm-qt.1
