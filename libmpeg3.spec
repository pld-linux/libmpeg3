Summary:	LibMPEG3 decodes the many many derivatives of MPEG standards
Name:		libmpeg3
Version:	1.2.2
Release:	1
License:	GPL
Group:		Libraries
URL:		http://heroine.linuxave.net/libmpeg3.html
Source0:	http://heroine.linuxave.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-shared.patch
Patch1:		%{name}-headers.patch
Patch2:		%{name}-install.patch
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

%package devel
Summary:	Header files for developing programs using libmpeg3
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package is all you need to develop programs that handle the
various video and audio file formats supported by libmpeg3.

%package static
Summary:	Static libmpeg3 library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libmpeg3 library.

%package progs
Summary:	libgr utility programs
Group:		Applications/Graphics
Requires:	%{name} = %{version}

%description progs
This package includes various utility programs for manipulating MPEG
files for use by libmpeg3 programs.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
ln -sf . libmpeg3

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -I./ -I../"

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
