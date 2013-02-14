%bcond_with internet
%global packname  pkgDepTools
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.24.0
Release:          1
Summary:          Package Dependency Tools
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/pkgDepTools_1.24.0.tar.gz
Requires:         R-methods R-graph R-RBGL R-Biobase R-Rgraphviz R-RCurl
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-methods R-graph R-RBGL R-Biobase R-Rgraphviz R-RCurl

%description
This package provides tools for computing and analyzing dependency
relationships among R packages.  It provides tools for building a
graph-based representation of the dependencies among all packages in a
list of CRAN-style package repositories.  There are also utilities for
computing installation order of a given package.  If the RCurl package is
available, an estimate of the download size required to install a given
package and its dependencies can be obtained.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{with internet}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
