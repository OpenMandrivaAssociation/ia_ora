Summary:        Ia Ora theme for kde
Name:           ia_ora
Version:        1.0
Release:        %mkrel 9
License:        GPL
Group:          Graphical desktop/Other
URL:            http://www.mandrivalinux.com/
BuildRequires:  kdelibs-devel
BuildRequires:  kdebase-devel >= 3.1.94-11mdk
Source0:        %{name}.tar.bz2

%description
Mandriva Ia Ora theme

 
%package kde
Summary: 	Mandriva theme for KDE - Widget design
Group: 		Graphical desktop/KDE

%description kde
Mandriva theme for KDE - Widget design

%package kde-kwin
Summary:	Mandriva theme for KDE - Window Decorations
Group:		Graphical desktop/KDE

%description kde-kwin
Mandriva theme for KDE - Window Decorations


%prep
%setup -q -n%name 

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

%files kde-kwin
%defattr(-,root,root,-)
%_libdir/kde3/kwin3_iaora.la
%_libdir/kde3/kwin3_iaora.so
%_libdir/kde3/kwin_iaora_config.la
%_libdir/kde3/kwin_iaora_config.so
%_datadir/apps/kwin/iaora.desktop



%files kde
%defattr(-,root,root,-)
%_libdir/kde3/plugins/styles/ia_ora.la
%_libdir/kde3/plugins/styles/ia_ora.so
%_datadir/apps/kstyle/themes/ia_ora.themerc

