%define	module	Pango
%define	perl_glib_require 1.220
%define upstream_version 1.226

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	31
Summary:	Perl module for the Pango library

License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	http://sourceforge.net/projects/gtk2-perl/files/Pango/%{upstream_version}/Pango-%{upstream_version}.tar.gz
Source1:	perl-Pango.rpmlintrc
URL:		http://gtk2-perl.sf.net/
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= %{perl_glib_require}
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	perl-Cairo
# for test suite:
#BuildRequires:	fontconfig
#BuildRequires:	fonts-ttf-dejavu
Requires:	perl-Glib >= %{perl_glib_require}

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
%setup -q -n %{module}-%{upstream_version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="%{optflags}"

%check
#xvfb-run %make test

%install
%makeinstall_std

%files
%doc AUTHORS LICENSE
%{perl_vendorarch}/%{module}
%{perl_vendorarch}/%{module}.pm
%exclude %{perl_vendorarch}/%{module}/*.pod
%exclude %{perl_vendorarch}/%{module}/*/*.pod
%{perl_vendorarch}/auto/*

%files doc
%doc examples
%{_mandir}/*/*
%{perl_vendorarch}/%{module}/*.pod
%{perl_vendorarch}/%{module}/*/*.pod


