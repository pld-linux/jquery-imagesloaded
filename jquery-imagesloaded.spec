# TODO
# bundles:
#    "eventEmitter": "4.x",
#    "eventie": "desandro/eventie#>=1.0.3"
%define		plugin	imagesloaded
Summary:	JavaScript is all like "You images done yet or what?" 
Name:		jquery-%{plugin}
Version:	3.0.2
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/desandro/imagesloaded/archive/v%{version}/%{plugin}-%{version}.tar.gz
# Source0-md5:	383f1e80700ac765e575e816b0cac74f
Source1:	http://desandro.github.io/imagesloaded/imagesloaded.pkgd.min.js
# Source1-md5:	fda1461c0fd15dd0f1addff76249af07
Source2:	http://desandro.github.io/imagesloaded/imagesloaded.pkgd.js
# Source2-md5:	145291ef6f29c93c84c8b161551d432f
URL:		http://desandro.github.io/imagesloaded/
Requires:	jquery >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Detect when images have been loaded.

%package demo
Summary:	Demo for jQuery.%{plugin}
Summary(pl.UTF-8):	Pliki demonstracyjne dla pakietu jQuery.%{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for jQuery.%{plugin}.

%prep
%setup -q -n %{plugin}-%{version}
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_examplesdir}/%{name}-%{version}}

cp -p %{plugin}.pkgd.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js
cp -p %{plugin}.pkgd.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.src.js
ln -s %{plugin}-%{version}.src.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.src.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_appdir}
