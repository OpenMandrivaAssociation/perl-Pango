%bcond_with	test

%define	modname	Pango

Name:		perl-%{modname}
Version:	1.223
Release:	3
Summary:	Perl modname for the Pango library
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{modname}-%{version}.tar.gz
URL:		http://gtk2-perl.sf.net/
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib)
BuildRequires:	perl(Cairo)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	perl-Cairo
%if %{with test}
BuildRequires:	fontconfig
BuildRequires:	fonts-ttf-dejavu
%endif

%description
This module provides perl access to the gtk+-2.x library.

Pango is a library for laying out and rendering text, with an emphasis on
internationalization. Pango can be used anywhere that text layout is needed,
but using Pango in conjunction with Cairo and/or Gtk2 provides a complete
solution with high quality text handling and graphics rendering.

%package	doc
Summary:	Pango documentation
Group:		Books/Computer books

%description	doc
This package contains documentation of the Pango module.


%prep
%setup -qn %{modname}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%if %{with test}
%check
xvfb-run %make test
%endif

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE
%dir %{perl_vendorarch}/%{modname}
%{perl_vendorarch}/%{modname}.pm
%dir %{perl_vendorarch}/%{modname}/Cairo
%dir %{perl_vendorarch}/%{modname}/Install
%{perl_vendorarch}/%{modname}/Install/*
%{perl_vendorarch}/auto/*

%files doc
%doc examples
%{_mandir}/*/*
%dir %{perl_vendorarch}/%{modname}
%{perl_vendorarch}/%{modname}/*.pod
%{perl_vendorarch}/%{modname}/Cairo/*pod

%changelog
* Wed Dec 26 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.223-3
- rebuild for perl-5.16.2
- cleanups

* Fri Jun 08 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.223-1
+ Revision: 803541
- cleanups
- fix %%files
- new version

* Mon Jan 23 2012 Götz Waschk <waschk@mandriva.org> 1.221-9
+ Revision: 766877
- update build deps
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.221-6
+ Revision: 667287
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.221-5mdv2011.0
+ Revision: 564572
- rebuild for perl 5.12.1

* Wed Jul 21 2010 Thierry Vignaud <tv@mandriva.org> 1.221-4mdv2011.0
+ Revision: 556531
- rebuild for new perl

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for perl 5.12

  + Sandro Cazzaniga <kharec@mandriva.org>
    - rebuild

* Thu Aug 13 2009 Thierry Vignaud <tv@mandriva.org> 1.221-1mdv2010.1
+ Revision: 416080
- new release

* Wed Mar 18 2009 Thierry Vignaud <tv@mandriva.org> 1.220-1mdv2009.1
+ Revision: 357205
- bump require on Glib binding
- new release (no change, just tagged as stable)

* Wed Mar 11 2009 Thierry Vignaud <tv@mandriva.org> 1.211-1mdv2009.1
+ Revision: 353613
- new release

* Fri Jan 16 2009 Thierry Vignaud <tv@mandriva.org> 1.210-1mdv2009.1
+ Revision: 330313
- BR pango-devel
- import perl-Pango


* Fri Jan 16 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.210-1mdv2009.1
- initial release
