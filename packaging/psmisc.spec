Name:    psmisc
Version: 22.20
Release: 2
License: GPL-2.0+
Summary: Utilities for managing processes on your system
Group:   Applications/System
URL:     http://sourceforge.net/projects/psmisc
Source:  http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1001: %{name}.manifest

BuildRequires: gettext
BuildRequires: ncurses-devel
BuildRequires: autoconf automake

#The following has been reworked by upstream in a different way ... we'll see
#Patch1: psmisc-22.13-fuser-silent.patch

# Patch sent upstream 2012-10-08.

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
cp %{SOURCE1001} .
#export LDFLAGS=" -pie"
%configure \
        --prefix=%{_prefix} \
        --disable-nls
make %{?_smp_mflags}

%install
make install DESTDIR="$RPM_BUILD_ROOT"

mkdir -p $RPM_BUILD_ROOT/sbin
mv $RPM_BUILD_ROOT%{_bindir}/fuser $RPM_BUILD_ROOT/sbin

mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
for keyword in LICENSE COPYING COPYRIGHT;
do
        for file in `find %{_builddir} -name $keyword`;
        do
                cat $file >> $RPM_BUILD_ROOT%{_datadir}/license/%{name};
                echo "";
        done;
done

%files
%manifest %{name}.manifest
%{_datadir}/license/%{name}
/sbin/fuser
%{_bindir}/killall
%{_bindir}/pstree
%{_bindir}/pstree.x11
%{_bindir}/prtstat
%{_mandir}/man1/fuser.1*
%{_mandir}/man1/killall.1*
%{_mandir}/man1/pstree.1*
%{_mandir}/man1/prtstat.1*
%ifarch %{ix86} x86_64 ppc ppc64 %{arm} mipsel
%{_bindir}/peekfd
%endif
%{_mandir}/man1/peekfd.1*
%doc AUTHORS ChangeLog COPYING README

%changelog
