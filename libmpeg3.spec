Summary:	LibMPEG3 decodes the many many derivatives of MPEG standards
Summary(pl):	LibMPEG3 dekoduje wiele alternatywnych standardów MPEG
Name:		libmpeg3
Version:	1.2.3
Release:	5
License:	GPL
Group:		Libraries
Source0:	http://heroinewarriors.com/%{name}-%{version}.tar.gz
URL:		http://heroinewarriors.com/libmpeg3.php3
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
- MPEG-2 video,
- MPEG-1 video,
- mp3 audio,
- mp2 audio,
- ac3 audio,
- MPEG-2 system streams,
- MPEG-1 system streams.

%description -l pl
LibMPEG3 dekoduje wiele odmian standardu MPEG w nieskompresowany
strumieñ, który ³atwo jest odtwarzaæ lub edytowaæ.

%package devel
Summary:	Header files for developing programs using libmpeg3
Summary(pl):	Pliki nag³ówkowe do rozwijania programów u¿ywaj±cych libmpeg3
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that handle the
various video and audio file formats supported by libmpeg3.

%description devel -l pl
Ten pakiet to wszystko czego potrzebujesz by rozwijaæ programy
obs³uguj±ce ró¿ne formaty plików wideo oraz audio wspierane przez
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
Summary(pl):	programy u¿ytkowe
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
This package includes various utility programs for manipulating MPEG
files for use by libmpeg3 programs.

%description progs -l pl
Ten pakiet zawiera ró¿ne programy narzêdziowe do manipulowania plikami
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
	--nocss \
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
