### Comment
# This file is modified automatically by 'xemacs-adapter' script
# from PLD-project CVS repository: cvs.pld.org.pl, module SPECS
# For more details see comments in this script
### EndComment

Summary: 	Wnn (4.2 and 6) support. SJ3 support.
Summary(pl):	Wnn (4.2 and 6) support. SJ3 support.

Name:    	xemacs-egg-its-pkg
%define 	srcname	egg-its
Version: 	1.22
Release:	1

### Preamble
Copyright:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires: 	xemacs
Requires: 	xemacs-leim-pkg
Requires: 	xemacs-mule-base-pkg
Requires: 	xemacs-fsf-compat-pkg
Requires: 	xemacs-base-pkg
### EndPreamble

%description


%description -l pl 


### Main
%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
gzip -9nf lisp/egg-its/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT
### EndMain

### PrePost
### EndPrePost

### Files
%files
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
%doc lisp/egg-its/ChangeLog.gz 
### EndFiles
