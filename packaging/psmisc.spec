Name:           psmisc
Version:        22.6
Release:        1
License:        BSD/GPLv2+
Summary:        Utilities for managing processes on your system
Url:            http://psmisc.sourceforge.net
Group:          Applications/System
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(ncurses)

%description
The psmisc package contains utilities for managing processes on your
system: pstree, killall and fuser.  The pstree command displays a tree
structure of all of the running processes on your system.  The killall
command sends a specified signal (SIGTERM if nothing is specified) to
processes identified by name.  The fuser command identifies the PIDs
of processes that are using specified files or filesystems.

%prep
%setup -q

%build
%configure --prefix=/usr
make %{?_smp_mflags}

%install
%make_install

mkdir -p %{buildroot}/bin
mv %{buildroot}%{_bindir}/fuser %{buildroot}/bin/
mkdir -p %{buildroot}/usr/share/pixmaps/
install -m 644 icons/pstree16.xpm %{buildroot}/usr/share/pixmaps/
install -m 644 icons/pstree32.xpm %{buildroot}/usr/share/pixmaps/


%remove_docs

%files 
/bin/fuser
%{_bindir}/killall
%{_bindir}/oldfuser
%{_bindir}/pstree
%{_bindir}/pstree.x11
%{_prefix}/share/locale/*/LC_MESSAGES/*
%{_prefix}/share/pixmaps/pstree*.xpm
