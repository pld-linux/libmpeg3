Summary:	LibMPEG3 - decoding of many many derivatives of MPEG standards
Summary(pl.UTF-8):	LibMPEG3 - dekodowanie wielu alternatywnych standardów MPEG
Name:		libmpeg3
Version:	1.8
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/heroines/%{name}-%{version}-src.tar.bz2
# Source0-md5:	a9d0d34e8941a4437eb8e7dfe559eca1
Patch0:		%{name}-acam.patch
Patch1:		format-security.patch
URL:		http://heroinewarrior.com/libmpeg3.php
BuildRequires:	a52dec-libs-devel >= 0.7.3
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
%ifarch i586 i686 athlon
BuildRequires:	nasm
%endif
Requires:	a52dec-libs >= 0.7.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibMPEG3 decodes the many many derivatives of MPEG standards into
uncompressed data suitable for editing and playback.

libmpeg3 currently decodes:
 - MPEG-1 Layer II Audio
 - MPEG-1 Layer III Audio
 - MPEG-2 Layer III Audio
 - MPEG-1 program streams
 - MPEG-2 program streams
 - MPEG-2 transport streams
 - AC3 Audio
 - MPEG-2 Video
 - MPEG-1 Video
 - IFO files
 - VOB files

%description -l pl.UTF-8
LibMPEG3 dekoduje wiele odmian standardu MPEG w nieskompresowany
strumień, który łatwo jest odtwarzać lub modyfikować. Aktualnie
potrafi dekodować: dźwięk MPEG-1 Layer II i III oraz MPEG-2 Layer 3,
strumienie MPEG-1 i MPEG-2, dźwięk AC3, obraz MPEG-1 i MPEG-2, pliki
IFO oraz VOB.

%package devel
Summary:	Header files for developing programs using libmpeg3
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania programów używających libmpeg3
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	a52dec-libs-devel >= 0.7.3

%description devel
This package is all you need to develop programs that handle the
various video and audio file formats supported by libmpeg3.

%description devel -l pl.UTF-8
Ten pakiet to wszystko czego potrzebujesz by rozwijać programy
obsługujące różne formaty plików wideo oraz audio wspierane przez
libmpeg3.

%package static
Summary:	Static libmpeg3 library
Summary(pl.UTF-8):	Statyczna biblioteka libmpeg3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmpeg3 library.

%description static -l pl.UTF-8
Statyczna biblioteka libmpeg3.

%package progs
Summary:	libmpeg3 utility programs
Summary(pl.UTF-8):	Programy użytkowe based on libmpeg3
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description progs
This package includes various utility programs for manipulating MPEG
files for use by libmpeg3 programs.

%description progs -l pl.UTF-8
Ten pakiet zawiera różne programy narzędziowe do manipulowania plikami
MPEG.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"
%configure \
%ifarch i586 i686 athlon
	--enable-mmx
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmpeg3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmpeg3.so.1

%files devel
%defattr(644,root,root,755)
%doc docs/index.html
%attr(755,root,root) %{_libdir}/libmpeg3.so
%{_libdir}/libmpeg3.la
%{_includedir}/libmpeg3

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpeg3.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mpeg3cat
%attr(755,root,root) %{_bindir}/mpeg3dump
%attr(755,root,root) %{_bindir}/mpeg3peek
%attr(755,root,root) %{_bindir}/mpeg3toc
