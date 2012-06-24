Summary:	LibMPEG3 decodes the many many derivatives of MPEG standards
Summary(pl):	LibMPEG3 dekoduje wiele alternatywnych standard�w MPEG
Name:		libmpeg3
Version:	1.5
Release:	3
License:	GPL
Group:		Libraries
Source0:	http://heroinewarrior.com/%{name}-%{version}.tar.gz 
URL:		http://heroinewarriors.com/libmpeg3.php3
Patch0:		%{name}-install.patch
Patch1:		%{name}-opt.patch
Patch2:		%{name}-shared.patch
BuildRequires:	nasm
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

%description -l pl
LibMPEG3 dekoduje wiele odmian standardu MPEG w nieskompresowany
strumie�, kt�ry �atwo jest odtwarza� lub edytowa�. Aktualnie potrafi
dekodowa�: d�wi�k MPEG-1 Layer II i III oraz MPEG-2 Layer 3,
strumienie MPEG-1 i MPEG-2, d�wi�k AC3, obraz MPEG-1 i MPEG-2, pliki
IFO oraz VOB.

%package devel
Summary:	Header files for developing programs using libmpeg3
Summary(pl):	Pliki nag��wkowe do rozwijania program�w u�ywaj�cych libmpeg3
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that handle the
various video and audio file formats supported by libmpeg3.

%description devel -l pl
Ten pakiet to wszystko czego potrzebujesz by rozwija� programy
obs�uguj�ce r�ne formaty plik�w wideo oraz audio wspierane przez
libmpeg3.

%package static
Summary:	Static libmpeg3 library
Summary(pl):	Statyczna biblioteka libmpeg3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libmpeg3 library.

%description static -l pl
Statyczna biblioteka libmpeg3.

%package progs
Summary:	libmpeg3 utility programs
Summary(pl):	programy u�ytkowe
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
This package includes various utility programs for manipulating MPEG
files for use by libmpeg3 programs.

%description progs -l pl
Ten pakiet zawiera r�ne programy narz�dziowe do manipulowania plikami
MPEG.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	OPT="%{rpmcflags} %{!?debug:-fomit-frame-pointer}" \
%ifarch i586 i686 athlon
	USE_MMX=1
%endif

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
%attr(755,root,root) %{_libdir}/libmpeg3.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/index.html
%attr(755,root,root) %{_libdir}/libmpeg3.so
%{_includedir}/libmpeg3

%files static
%defattr(644,root,root,755)
%{_libdir}/libmpeg3.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
