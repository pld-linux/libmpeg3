Summary:	LibMPEG3 decodes the many many derivatives of MPEG standards
Summary(pl):	LibMPEG3 dekoduje wiele alternatywnych standardÛw MPEG
Name:		libmpeg3
Version:	1.2.3
Release:	3
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
URL:		http://heroine.linuxave.net/libmpeg3.html
Source0:	http://heroine.linuxave.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-install.patch
Patch3:		%{name}-gcc.patch
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
strumieÒ, ktÛry ≥atwo jest odtwarzaÊ lub edytowaÊ.

%package devel
Summary:	Header files for developing programs using libmpeg3
Summary(pl):	Pliki nag≥Ûwkowe do rozwijania programÛw uøywaj±cych libmpeg3
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that handle the
various video and audio file formats supported by libmpeg3.

%description -l pl devel
Ten pakiet to wszystko czego potrzebujesz by rozwijaÊ programy
obs≥uguj±ce rÛøne formaty plikÛw wideo oraz audio wspierane przez
libmpeg3.

%package static
Summary:	Static libmpeg3 library
Summary(pl):	Statyczna biblioteka libmpeg3
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static libmpeg3 library.

%description -l pl static
Statyczna biblioteka libmpeg3.

%package progs
Summary:	libmpeg3 utility programs
Summary(pl):	programy uøytkowe
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Requires:	%{name} = %{version}

%description progs
This package includes various utility programs for manipulating MPEG
files for use by libmpeg3 programs.

%description -l pl progs
Ten pakiet zawiera rÛøne programy narzÍdziowe do manipulowania plikami
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
