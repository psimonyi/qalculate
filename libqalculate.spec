Summary: Multi-purpose calculator library
Name: libqalculate
Version: 0.9.5
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://qalculate.sourceforge.net/
Source0: http://dl.sf.net/sourceforge/qalculate/libqalculate-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glib2-devel, cln-devel
BuildRequires: libxml2-devel
BuildRequires: readline-devel, ncurses-devel
BuildRequires: perl(XML::Parser), gettext

%description
This library underpins the Qalculate! multi-purpose desktop calculator for
GNU/Linux

%package devel
Summary: Development tools for the Qalculate calculator library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: glib2-devel, libxml2-devel, cln-devel

%description devel
The libqalculate-devel package contains the header files needed for development
with libqalculate.

%package -n qalculate
Summary: Multi-purpose calculator, text mode interface
Group: Applications/Engineering
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description -n qalculate
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides the text-mode interface for Qalculate!

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{name}
rm -f %{buildroot}/%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{_libdir}/libqalculate.so.*
%{_datadir}/qalculate/

%files devel
%defattr(-,root,root,-)
%{_libdir}/libqalculate.so
%{_libdir}/pkgconfig/libqalculate.pc
%{_includedir}/libqalculate/

%files -n qalculate
%defattr(-,root,root,-)
%{_bindir}/qalc

%changelog
* Tue Jan 02 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.5-1
- New release

* Mon Aug 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-4
- Rebuild for FC6

* Thu Jun 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-3
- Arbitrarily bump the release field to fix broken update path

* Wed Jun 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-1
- New version 0.9.4

* Tue Apr 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.3-2
- More BRs from Paul Howarth (#193481)

* Thu Mar 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.3-1
- Update to newer version

* Mon Feb 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.2-2
- Rebuild for Fedora Extras 5

* Tue Dec 27 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.2-1
- Upgrade to new version

* Sat Nov 05 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.0-1
- Upgrade to new version

* Mon Oct 17 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-3
- Add patch to allow build with cln-1.1.10

* Mon Oct 17 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-2
- Bump the release tag to make even with FC-4 and FC-3 branches

* Tue Oct 11 2005 Paul Howarth <paul@city-fan.org> - 0.8.2-1
- Split off separate qalculate subpackage
- Update to 0.8.2

* Mon Oct 10 2005 Paul Howarth <paul@city-fan.org> - 0.8.1.2-2
- Don't include static libraries
- Include license text
- Don't include README, which only contains a URL
- Include AUTHORS & TODO
- Remove redundant manual dependencies
- Split off separate devel subpackage
- Be more explicit in %%files list
- Add %%post and %%postun scripts to run ldconfig
- Use DESTDIR with make instead of %%makeinstall
- Add buildreqs readline-devel and ncurses-devel

* Wed Oct 05 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.1.2-1
- Initial package
