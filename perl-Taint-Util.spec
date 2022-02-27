#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Taint
%define		pnam	Util
Summary:	Taint::Util - Test for and flip the taint flag without regex matches or eval
Summary(pl.UTF-8):	Taint::Util - sprawdzanie i zmiana flagi skażenia bez wyrażeń regularnych ani eval
Name:		perl-Taint-Util
Version:	0.08
Release:	9
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Taint/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f081a8a6e82352741c0486784cbc23d
URL:		https://metacpan.org/dist/Taint-Util
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.11
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Taint::Util wraps Perl's internal routines for checking and setting
the taint flag and thus does not rely on regular expressions for
untainting or odd tricks involving eval and kill for checking whether
data is tainted, instead it checks and flips a flag on the scalar
in-place.

%description -l pl.UTF-8
Taint::Util obudowuje wewnętrzne procedury Perla do sprawdzania i
ustawiania flagi skażenia, dzięki czemu nie polega na wyrażeniach
regularnych w celu usuwania flagi lub brzydkich sztuczkach z eval i
kill w celu sprawdzenia, czy dane są skażone - zamiast tego sprawdza
i przełącza flagę zmiennych skalarnych w miejscu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%dir %{perl_vendorarch}/Taint
%{perl_vendorarch}/Taint/Util.pm
%dir %{perl_vendorarch}/auto/Taint
%dir %{perl_vendorarch}/auto/Taint/Util
%attr(755,root,root) %{perl_vendorarch}/auto/Taint/Util/Util.so
%{_mandir}/man3/Taint::Util.3pm*
