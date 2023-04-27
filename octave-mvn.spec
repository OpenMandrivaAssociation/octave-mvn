%global octpkg mvn

Summary:	Multivariate normal distribution clustering and utility functions
Name:		octave-mvn
Version:	1.1.0
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/mvn/
Source0:	https://downloads.sourceforge.net/octave/mvn-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.6.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Multivariate normal distribution clustering and utility functions.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

