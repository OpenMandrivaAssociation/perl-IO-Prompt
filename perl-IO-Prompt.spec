%define upstream_name    IO-Prompt
%define upstream_version 0.997001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Interactively prompt for user input
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::Handle)
BuildRequires: perl(POSIX)
BuildRequires: perl(Term::ReadKey)
BuildRequires: perl(Test::More)
BuildRequires: perl(Want)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/IO
