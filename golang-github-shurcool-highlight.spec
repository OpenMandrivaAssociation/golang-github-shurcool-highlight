# Run tests in check section
%bcond_without check

%global goipath         github.com/shurcooL/highlight_go
%global commit          78fb10f4a5f89e812a5e26ab723b954a51226086

%global common_description %{expand:
Syntax highlighter for Go, using go/scanner.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Syntax highlighter for Go, using go/scanner
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/sourcegraph/annotate)
BuildRequires: golang(github.com/sourcegraph/syntaxhighlight)

%if %{with check}
BuildRequires: golang(github.com/sourcegraph/syntaxhighlight)
%endif

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git78fb10f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180418git78fb10f
- First package for Fedora

