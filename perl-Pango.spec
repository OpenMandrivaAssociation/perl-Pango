%define module	Pango
%define	name	perl-%{module}
%define	version	1.221
%define	release	%mkrel 1
%define perl_glib_require 1.220

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl module for the Pango library
License:	GPL or Artistic
Group:	  	Development/GNOME and GTK+
Source:		http://prdownloads.sourceforge.net/gtk2-perl/%{module}-%{version}.tar.gz
URL:		http://gtk2-perl.sf.net/
BuildRequires:	perl-devel
BuildRequires:	perl-ExtUtils-Depends >= 0.300
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.03
BuildRequires:	perl-Glib >= %perl_glib_require
BuildRequires:	pango-devel perl-Cairo
# for test suite:
#BuildRequires:	fontconfig
#BuildRequires:	fonts-ttf-dejavu
Requires:	perl-Glib >= %perl_glib_require
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides perl access to the gtk+-2.x library.

Pango is a library for laying out and rendering text, with an emphasis on
internationalization. Pango can be used anywhere that text layout is needed,
but using Pango in conjunction with Cairo and/or Gtk2 provides a complete
solution with high quality text handling and graphics rendering.

%package doc
Summary: Pango documentation
Group: Books/Computer books

%description doc
This package contains documentation of the Pango module.


%prep
%setup -q -n %{module}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make OPTIMIZE="%{optflags}"

%check
#xvfb-run %make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-, root, root)
%doc AUTHORS LICENSE
%dir %{perl_vendorarch}/%{module}
%{perl_vendorarch}/%{module}.pm
%{perl_vendorarch}/%{module}/*/*.pm
%{perl_vendorarch}/%{module}/Install
%{perl_vendorarch}/auto/*

%files doc
%defattr(-, root, root)
%doc examples
%{_mandir}/*/*
%dir %{perl_vendorarch}/%{module}
%{perl_vendorarch}/%{module}/*.pod
%{perl_vendorarch}/%{module}/*/*.pod


