Summary: A multi-purpose desktop calculator for GNU/Linux
Name: qalculate-gtk
Version: 0.9.4
Release: 4%{?dist}
License: GPL
Group: Applications/Engineering
URL: http://qalculate.sourceforge.net/
Source: http://dl.sf.net/qalculate/qalculate-gtk-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: libgnome-devel, libglade2-devel, libqalculate-devel
BuildRequires: libgnomeui-devel
BuildRequires: gettext, desktop-file-utils, scrollkeeper
Requires: gnuplot
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting.
This package provides a (GTK+) graphical interface for Qalculate! 

%prep
%setup -q

%build
%configure 
make %{?_smp_mflags}
										
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

desktop-file-install --delete-original                   \
        --vendor fedora                                  \
        --dir %{buildroot}%{_datadir}/applications       \
	--mode 0644				         \
        --add-category X-Fedora                          \
        %{buildroot}%{_datadir}/applications/qalculate-gtk.desktop

%find_lang qalculate-gtk
rm -rf %{buildroot}/%{_bindir}/qalculate

install -Dp -m 0644 data/icon.xpm %{buildroot}%{_datadir}/pixmaps/qalculate.xpm

%post
scrollkeeper-update -q -o %{_datadir}/omf/qalculate-gtk || :

%postun
scrollkeeper-update -q || :

%clean
rm -rf %{buildroot}

%files -f qalculate-gtk.lang
%defattr(-, root, root, -)
%doc AUTHORS ChangeLog COPYING TODO
%doc %{_datadir}/gnome/help/qalculate-gtk/
%{_bindir}/qalculate-gtk
%{_datadir}/applications/fedora-qalculate-gtk.desktop
%{_datadir}/pixmaps/qalculate.xpm
%{_datadir}/pixmaps/qalculate.png
%{_datadir}/omf/qalculate-gtk/
%{_datadir}/qalculate-gtk/

%changelog
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
