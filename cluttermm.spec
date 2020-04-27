Summary:	C++ wrappers for Clutter library
Summary(pl.UTF-8):	Obudowanie C++ do biblioteki Clutter
Name:		cluttermm
Version:	1.17.3
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cluttermm/1.17/%{name}-%{version}.tar.xz
# Source0-md5:	429fa3a4ee1fad9ca2bc46b174165dfd
URL:		https://developer.gnome.org/cluttermm/
BuildRequires:	atkmm-devel >= 2.22.2
BuildRequires:	clutter-devel >= 1.18.0
# for examples
BuildRequires:	gtkmm3-devel >= 3.10
BuildRequires:	libstdc++-devel
BuildRequires:	mm-common >= 0.8
BuildRequires:	pangomm-devel >= 2.27.1
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	atkmm >= 2.22.2
Requires:	clutter >= 1.18.0
Requires:	pangomm >= 2.27.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C++ wrappers for Clutter library.

%description -l pl.UTF-8
Obudowanie C++ do biblioteki Clutter.

%package devel
Summary:	Header files for cluttermm library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki cluttermm
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	atkmm-devel >= 2.22.2
Requires:	clutter-devel >= 1.18.0
Requires:	pangomm-devel >= 2.27.1

%description devel
Header files for cluttermm library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki cluttermm.

%package static
Summary:	Static cluttermm library
Summary(pl.UTF-8):	Statyczna biblioteka cluttermm
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static cluttermm library.

%description static -l pl.UTF-8
Statyczna biblioteka cluttermm.

%package apidocs
Summary:	cluttermm API documentation
Summary(pl.UTF-8):	Dokumentacja API cluttermm
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
cluttermm API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API cluttermm.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libcluttermm-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcluttermm-1.0.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcluttermm-1.0.so
%dir %{_libdir}/cluttermm-1.0
%{_libdir}/cluttermm-1.0/include
%{_includedir}/cluttermm-1.0
%{_datadir}/cluttermm-1.0
%{_pkgconfigdir}/cluttermm-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libcluttermm-1.0.a

%files apidocs
%defattr(644,root,root,755)
%{_docdir}/cluttermm-1.0
%{_datadir}/devhelp/books/cluttermm-1.0
