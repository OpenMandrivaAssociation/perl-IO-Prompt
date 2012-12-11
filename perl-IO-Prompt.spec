%define upstream_name    IO-Prompt
%define upstream_version 0.997001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Interactively prompt for user input
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(POSIX)
BuildRequires:	perl(Term::ReadKey)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Want)

BuildArch:	noarch

%description
By default, this module exports a single function 'prompt'. It prompts the
user to enter some input, and returns an object that represents the user
input.

You may specify various flags to the function to affect its behaviour; most
notably, it defaults to automatically 'chomp' the input, unless the '-line'
flag is specified.

Two other functions are exported at request: 'hand_print', which simulates
hand-typing to the console; and 'get_input', which is the lower-level
function that actually prompts the user for a suitable input.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# requires /dev/tty
rm t/01.dependencies.t

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/IO


%changelog
* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.997.1-1mdv2010.1
+ Revision: 539084
- update to 0.997001

* Mon Feb 01 2010 Jérôme Quelin <jquelin@mandriva.org> 0.997.0-1mdv2010.1
+ Revision: 498978
- update to 0.997

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.996.0-1mdv2010.1
+ Revision: 489526
- remove test failing in non-interactive setup
- update to 0.996

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> v0.99.4-3mdv2010.0
+ Revision: 430473
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> v0.99.4-2mdv2009.0
+ Revision: 268530
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> v0.99.4-1mdv2009.0
+ Revision: 194417
- import perl-IO-Prompt


* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> v0.99.4-1mdv2009.0
- first mdv release
