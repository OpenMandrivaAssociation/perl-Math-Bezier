%define upstream_name	 Math-Bezier
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Solution of Bezier Curves
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	ftp.perl.org/pub/CPAN/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements the algorithm for the solution of Bezier curves
as presented by Robert D. Miller in Graphics Gems V, "Quick and Simple
Bezier Curve Drawing". 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Math
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 403850
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-13mdv2009.0
+ Revision: 257775
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-12mdv2009.0
+ Revision: 245825
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-10mdv2008.1
+ Revision: 133638
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-9mdv2008.0
+ Revision: 86575
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-8mdv2007.0
- Rebuild

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-7mdk
- Fix According to perl Policy
	- Source URL

* Tue Dec 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-6mdk
- better summary  
- %%mkrel
- spec cleanup
- enable tests

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-5mdk
- fix buildrequires in a backward compatible way

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-4mdk 
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.01-3mdk
- fixed dir ownership (distlint)
- %%makeinstall_std macro

