%define libname_kwin %mklibname %{name}-kde
%define libname_kde %mklibname %{name}-kwin

Summary:        iIa Ora theme for kde
Name:           ia_ora
Version:        1.0
Release:        %mkrel 10
License:        GPL
Group:          Graphical desktop/Other
URL:            http://www.mandrivalinux.com/
BuildRequires:  kdelibs-devel
BuildRequires:  kdebase-devel >= 3.1.94-11mdk
Source0:        %{name}.tar.bz2
Patch0:         %{name}-fix-makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mandriva Ia Ora theme

#--------------------------------------------------------------------
 
%package kde
Summary: 	Mandriva theme for KDE - Widget design
Group: 		Graphical desktop/KDE
Requires:       %libname_kde >= %version

%description kde
Mandriva theme for KDE - Widget design

%files kde
%defattr(-,root,root,-)
%_datadir/apps/kstyle/themes/ia_ora.themerc

#--------------------------------------------------------------------

%package -n %libname_kde
Summary:        Mandriva theme for KDE - Widget design
Group:          System/Libraries
Conflicts:      %name-kde < 1.0-10

%description -n %libname_kde
Mandriva theme for KDE - Widget design

%files -n %libname_kde
%defattr(-,root,root,-)
%_libdir/kde3/plugins/styles/ia_ora.la
%_libdir/kde3/plugins/styles/ia_ora.so

#--------------------------------------------------------------------

%package kde-kwin
Summary:	Mandriva theme for KDE - Window Decorations
Group:		Graphical desktop/KDE
Requires:       %libname_kwin >= %version

%description kde-kwin
Mandriva theme for KDE - Window Decorations

%files kde-kwin
%defattr(-,root,root,-)
%_datadir/apps/kwin/iaora.desktop

#--------------------------------------------------------------------

%package -n %libname_kwin
Summary:        Mandriva theme for KDE - Widget design
Group:          System/Libraries
Conflicts:      %name-kwin < 1.0-10

%description -n %libname_kwin
Mandriva theme for KDE - Widget design

%files -n %libname_kwin
%defattr(-,root,root,-)
%_libdir/kde3/kwin3_iaora.la
%_libdir/kde3/kwin3_iaora.so
%_libdir/kde3/kwin_iaora_config.la
%_libdir/kde3/kwin_iaora_config.so

#--------------------------------------------------------------------

%prep
%setup -q -n%name 
%patch0 -p0

%build
make -f admin/Makefile.common cvs

export QTDIR=%qtdir
export KDEDIR=%_prefix

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

%configure2_5x \
%if "%{_lib}" != "lib"
   --enable-libsuffix="%(A=%{_lib}; echo ${A/lib/})" \
%endif
	--with-xinerama
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT
