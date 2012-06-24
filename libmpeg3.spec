Summary:	LibMPEG3 decodes the many many derivatives of MPEG standards
Summary(pl):	LibMPEG3 dekoduje wiele alternatywnych standard�w MPEG
Name:		libmpeg3
Version:	1.2.3
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
URL:		http://heroine.linuxave.net/libmpeg3.html
Source0:	http://heroine.linuxave.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-gcc.patch
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
LibMPEG3 decodes the many many derivatives of MPEG standards into
uncompressed data suitable for editing and playback.

libmpeg3 currently decodes:

  MPEG-2 video
  MPEG-1 video
  mp3 audio
  mp2 audio
  ac3 audio
  MPEG-2 system streams
  MPEG-1 system streams

%description -l pl
LibMPEG3 dekoduje wiele odmian standardu MPEG w nieskompresowany
strumie�, kt�ry �atwo jest odtwarza� lub edytowa�.

%package devel
Summary:	Header files for developing programs using libmpeg3
Summary(pl):	Pliki nag��wkowe do rozwijania program�w u�ywaj�cych libmpeg3
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that handle the
various video and audio file formats supported by libmpeg3.

%description -l pl devel
Ten pakiet to wszystko czego potrzebujesz by rozwija� programy
obs�uguj�ce r�ne formaty plik�w wideo oraz audio wspierane przez
libmpeg3.

%package static
Summary:	Static libmpeg3 library
Summary(pl):	Statyczna biblioteka libmpeg3
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libmpeg3 library.

%description -l pl static
Statyczna biblioteka libmpeg3.

%package progs
Summary:	libmpeg3 utility programs
Summary(pl):	programy u�ytkowe
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Requires:	%{name} = %{version}

%description progs
This package includes various utility programs for manipulating MPEG
files for use by libmpeg3 programs.

%description -l pl progs
Ten pakiet zawiera r�ne programy narz�dziowe do manipulowania plikami
MPEG.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
ln -sf . libmpeg3

%build
CFLAGS="%{rpmcflags} -I./ -I../"
export CFLAGS
./configure \
%ifnarch %{ix86}
	--nommx \
	--nocss
%endif
	--nothing

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

gzip -9nf docs/*.html

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc docs/index.html.gz
%attr(755,root,root) %{_libdir}/lib*.so
%dir %{_includedir}/libmpeg3
%dir %{_includedir}/libmpeg3/audio
%dir %{_includedir}/libmpeg3/video
%{_includedir}/libmpeg3/*.h
%{_includedir}/libmpeg3/*.inc
%{_includedir}/libmpeg3/audio/*.h
%{_includedir}/libmpeg3/video/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
