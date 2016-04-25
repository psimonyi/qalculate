Summary:	Multi-purpose calculator library
Name:		libqalculate
Version:	0.9.7
Release:	18%{?dist}
License:	GPLv2+
Group:		System Environment/Libraries
URL:		http://qalculate.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch1:		libqalculate-0.9.7-pkgconfig_private.patch
Patch2:		libqalculate-htmldir.patch
# don't spam errors if euroref-daily.xml doesn't (yet) exist
Patch3:     libqalculate-0.9.7-euroref-daily.patch
Patch4:     gcc-6-compile.patch
Patch5:     libqalculate-buffer.patch

BuildRequires:	glib2-devel, cln-devel
BuildRequires:	libxml2-devel
BuildRequires:	readline-devel, ncurses-devel
BuildRequires:	perl(XML::Parser), gettext
BuildRequires:	perl(Getopt::Long)

%description
This library underpins the Qalculate! multi-purpose desktop calculator for
GNU/Linux

%package	devel
Summary:	Development tools for the Qalculate calculator library
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	glib2-devel, libxml2-devel, cln-devel

%description	devel
The libqalculate-devel package contains the header files needed for development
with libqalculate.

%package -n	qalculate
Summary:	Multi-purpose calculator, text mode interface
Group:		Applications/Engineering
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig

%description -n	qalculate
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides the text-mode interface for Qalculate! The GTK and QT
frontends are provided by qalculate-gtk and qalculate-kde packages resp.

%prep
%setup -q
%patch1 -p1 -b .pkgconfig_private
%patch2 -p0 -b .htmldir-unversioned
%patch3 -p1 -b .euroref-daily
%patch4
%patch5 -p1 -b .buffer

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
%find_lang %{name}
rm -f %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING TODO
%{_libdir}/libqalculate.so.*
%{_datadir}/qalculate/
%{_docdir}/%{name}/*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libqalculate.so
%{_libdir}/pkgconfig/libqalculate.pc
%{_includedir}/libqalculate/

%files -n qalculate
%defattr(-,root,root,-)
%{_bindir}/qalc

%changelog
* Mon Apr 25 2016 Than Ngo <than@redhat.com> - 0.9.7-18
- bz#953615, fix global variable buffer

* Thu Feb 18 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.7-17
- Add BR:perl(Getopt::Long)
- Added doc to %files section

* Tue Feb 16 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9.7-16
- Added patch to fix GCC-6 FTBFS. Thanks Yaakov Selkowitz

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.7-14
- workaround (mostly) needless stderr spam: failed to load external entity .../eurofxref-daily.xml

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 09 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.7-12
- rebuild(gcc5), tighten subpkg deps via %%{?_isa}

* Mon Feb 23 2015 Rex Dieter <rdieter@fedoraproject.org> 0.9.7-11
- rebuild (gcc5)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 15 2013 Deji Akingunola <dakingun@gmail.com> - 0.9.7-8
- Fix for versioned docdir build error

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Feb 13 2010 Rex Dieter <rdieter@fedorproject.org> - 0.9.7-2
- respin pkgconfig_private patch for implicit linkage (#564920)

* Fri Jan 29 2010 Deji Akingunola <dakingun@gmail.com> - 0.9.7-1
- Update to 0.9.7

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Rex Dieter <rdieter@fedoraproject.org> 0.9.6-7
- move auto*foo to prep stage
- trim pkg-config-related deps (#509840)

* Sun Jul 05 2009 Deji Akingunola <dakingun@gmail.com> - 0.9.6-6
- Rebuild for cln-1.3.0

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-4
- Rebuild (with patch) for cln-1.2

* Sun Feb 10 2008 Deji Akingunola <dakingun@gmail.com> - 0.9.6-3
- Rebuild for gcc43

* Sat Aug 25 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-2
- Rebuild

* Fri Aug 03 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-2
- License tag update

* Sun Jul 01 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.6-1
- Update to new release

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
