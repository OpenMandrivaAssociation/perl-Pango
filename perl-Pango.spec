%bcond_with	test
%define	modname	Pango

Summary:	Perl modname for the Pango library
Name:		perl-%{modname}
Version:	1.223
Release:	6
License:	GPLv2 or Artistic
Group:		Development/GNOME and GTK+
Url:		http://gtk2-perl.sf.net/
Source0:	http://prdownloads.sourceforge.net/gtk2-perl/%{modname}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Glib)
BuildRequires:	perl(Cairo)
BuildRequires:	pkgconfig(pangocairo)
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
%{_mandir}/man3/*
%dir %{perl_vendorarch}/%{modname}
%{perl_vendorarch}/%{modname}/*.pod
%{perl_vendorarch}/%{modname}/Cairo/*pod

