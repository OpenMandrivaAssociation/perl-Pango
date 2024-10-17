%define module Pango
%define perl_glib_require 1.220
%define upstream_version 1.227
%define _disable_ld_no_undefined 1
%define _disable_lto 1

Name:		perl-%{module}
Version:	%perl_convert_version %{upstream_version}
Release:	8
Summary:	Perl module for the Pango library
License:	GPL or Artistic
Group:		Development/GNOME and GTK+
Source0:	http://sourceforge.net/projects/gtk2-perl/files/Pango/%{upstream_version}/Pango-%{upstream_version}.tar.gz
Source1:	perl-Pango.rpmlintrc
URL:		https://gtk2-perl.sf.net/
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(ExtUtils::Depends) >= 0.300
BuildRequires:	perl(ExtUtils::PkgConfig) >= 1.03
BuildRequires:	perl(Glib) >= %{perl_glib_require}
BuildRequires:	perl(File::Spec)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	perl(Cairo)
BuildRequires:	gcc
# for test suite:
#BuildRequires:	fontconfig
#BuildRequires:	fonts-ttf-dejavu
Requires:	perl-Glib >= %{perl_glib_require}
Requires:	perl(Cairo)

%description
This module provides perl access to the gtk+-2.x library.

Pango is a library for laying out and rendering text, with an emphasis on
internationalization. Pango can be used anywhere that text layout is needed,
but using Pango in conjunction with Cairo and/or Gtk2 provides a complete
solution with high quality text handling and graphics rendering.

%package doc
Summary:	Pango documentation
Group:		Books/Computer books

%description doc
This package contains documentation of the Pango module.

%prep
%autosetup -n %{module}-%{upstream_version}

perl Makefile.PL INSTALLDIRS=vendor CC=gcc LD=gcc
# fix build:
sed -i 's!q(build/doc.pl!q(./build/doc.pl!' Makefile

%build
%make_build CC=gcc LD=gcc

%check
#xvfb-run make test

%install
%make_install

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
