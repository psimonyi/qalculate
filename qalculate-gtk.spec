Summary:	A multi-purpose desktop calculator for GNU/Linux
Name:		qalculate-gtk
Version:	0.9.7
Release:	8%{?dist}
License:	GPLv2+
Group:		Applications/Engineering
URL:		http://qalculate.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		qalculate-gtk-desktop.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	libgnome-devel, libglade2-devel, libgnomeui-devel
BuildRequires:	libqalculate-devel
BuildRequires:	gettext, desktop-file-utils, scrollkeeper
BuildRequires:	perl(XML::Parser), pkgconfig
Requires:	gnuplot

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides a (GTK+) graphical interface for Qalculate! 

%prep
%setup -q
%patch0 -p0 -b .desktop

%build
%configure 
make %{?_smp_mflags}
										
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

desktop-file-install --delete-original			\
%if 0%{?fedora} && 0%{?fedora} < 19
	--vendor fedora					\
%endif
	--remove-category Application			\
	--dir %{buildroot}%{_datadir}/applications	\
	--mode 0644					\
	%{buildroot}%{_datadir}/applications/qalculate-gtk.desktop

%find_lang qalculate-gtk
rm -rf %{buildroot}/%{_bindir}/qalculate

%clean
rm -rf %{buildroot}

%files -f qalculate-gtk.lang
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING TODO
%doc %{_datadir}/gnome/help/qalculate-gtk/
%{_bindir}/qalculate-gtk
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-qalculate-gtk.desktop
%else
%{_datadir}/applications/qalculate-gtk.desktop
%endif
%{_datadir}/pixmaps/qalculate.png
%{_datadir}/omf/qalculate-gtk/
%{_datadir}/qalculate-gtk/

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.7-7
- Remove --vendor from desktop-file-install https://fedorahosted.org/fesco/ticket/1077

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 0.9.7-3
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 29 2010 Deji Akingunola <dakingun@gmail.com> - 0.9.7-1
- Update to 0.9.7

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

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

* Sat Jun 09 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.5-2
- Modify the Name field in the desktop file to distinguish it from that of
  qalculate-kde (BZ #241024)
- Require 'yelp' for the Help menu (BZ #243395)

* Tue Jan 02 2007 Deji Akingunola <dakingun@gmail.com> - 0.9.5-1
- New release

* Mon Aug 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-5
- Add perl(XML::Parser) BR

* Mon Aug 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-4
- Rebuild for FC6

* Wed Jun 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-3
- Properly package up missing file

* Wed Jun 28 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-2
- Add missing BR on libgnomeui

* Wed Jun 27 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.4-1
- New version 0.9.4

* Thu Mar 30 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.3-1
- Update to newer version

* Mon Feb 13 2006 Deji Akingunola <dakingun@gmail.com> - 0.9.2-2
- Rebuild for Fedora Extras 5

* Tue Dec 27 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.2-1
- Upgrade to new version

* Sat Nov 05 2005 Deji Akingunola <dakingun@gmail.com> - 0.9.0.1
- Upgrade to new version

* Thu Nov 2 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2.1-2
- Rebuild with new cln package

* Thu Oct 13 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2.1-2
- Update to a new release that handles new behaviour in pango >= 1.10.0

* Thu Oct 13 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-4
- Fix for yelp error (Niklas Knutsson)

* Thu Oct 13 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-3
- Rmove explicit requires for gnome-vfs2 and libqalculate
- Install desktop file properly

* Tue Oct 11 2005 Paul Howarth <paul@city-fan.org> - 0.8.2-2
- Use "make DESTDIR=%%{buildroot}" instead of %%makeinstall
- Expand most references to %%{name} for clarity
- Make sure scriptlets complete successfully
- Add scriptlet deps
- Include license text
- Remove redundant doc files NEWS & README
- Fix directory ownership

* Tue Oct 11 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.2-1
- Upgraded to new version
- Remove redundant buildrequires - make libglade2 requires them all
- Remove the -export-dynamic configure option, now done upstream
- Add gnome-vfs2 to require.
- Install the desktop file

* Wed Oct 05 2005 Deji Akingunola <deji.aking@gmail.com> - 0.8.1
- Initial package
