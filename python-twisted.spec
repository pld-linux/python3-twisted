# TODO
# - split back to subpackages (python-tkinter, etc deps)
Summary:	Twisted is a networking engine written in Python
Name:		python-twisted
Version:	14.0.2
Release:	0.2
License:	MIT
Group:		Libraries/Python
Source0:	http://twistedmatrix.com/Releases/Twisted/14.0/Twisted-%{version}.tar.bz2
# Source0-md5:	8379eb15601d6b7543a189594d3fed8f
URL:		http://twistedmatrix.com/
BuildRequires:	rpmbuild(macros) >= 1.710
Patch0:		doc-lore-man-fix.patch
BuildRequires:	Zope-Interface >= 3.6.0
BuildRequires:	python-Crypto >= 2.6.1
BuildRequires:	python-devel >= 2.6
BuildRequires:	python-pyOpenSSL >= 0.10
Requires:	Zope-Interface >= 3.6.0
Requires:	python-pyOpenSSL >= 0.10
# python-TwistedConch
Requires:	python-Crypto
Requires:	python-pyasn1
Requires:	python-tkinter
# python-TwistedCore
Requires:	python-serial
# bring all provided resources back into the main package namespace.
# lore, news, runner not present in PLD, but O/P anyway
Provides:	python-TwistedConch = %{version}-%{release}
Provides:	python-TwistedCore = %{version}-%{release}
Provides:	python-TwistedCore-ssl = %{version}-%{release}
Provides:	python-TwistedMail = %{version}-%{release}
Provides:	python-TwistedNames = %{version}-%{release}
Provides:	python-TwistedWeb = %{version}-%{release}
Provides:	python-TwistedWeb2 = %{version}-%{release}
Provides:	python-TwistedWords = %{version}-%{release}
Provides:	python-twisted-lore = %{version}-%{release}
Provides:	python-twisted-news = %{version}-%{release}
Provides:	python-twisted-runner = %{version}-%{release}
Obsoletes:	python-TwistedConch < 14
Obsoletes:	python-TwistedCore < 14
Obsoletes:	python-TwistedCore-ssl < 14
Obsoletes:	python-TwistedMail < 14
Obsoletes:	python-TwistedNames < 14
Obsoletes:	python-TwistedWeb < 14
Obsoletes:	python-TwistedWeb2 < 14
Obsoletes:	python-TwistedWords < 14
Obsoletes:	python-twisted-lore < 14
Obsoletes:	python-twisted-news < 14
Obsoletes:	python-twisted-runner < 14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted is a networking engine written in Python, supporting numerous
protocols. It contains a web server, numerous chat clients, chat
servers, mail servers and more.

%prep
%setup -q -n Twisted-%{version}
%patch0 -p1

%build
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py_build

%if %{with tests}
# bin/trial twisted
# can't get this to work within the buildroot yet due to multicast
# https://twistedmatrix.com/trac/ticket/7494
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/twisted/*/test

%py_postclean

# no-manual-page-for-binary
install -d $RPM_BUILD_ROOT%{_mandir}/man1
for s in conch core lore mail; do
	cp -p doc/$s/man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
done

# devel-file-in-non-devel-package
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/runner/portmap.c
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/python/_initgroups.c
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/test/raiser.c
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/internet/iocpreactor/iocpsupport/winsock_pointers.c
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/internet/iocpreactor/iocpsupport/winsock_pointers.h
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/internet/iocpreactor/iocpsupport/iocpsupport.c
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/python/sendmsg.c

# pem-certificate
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/internet/test/fake_CAs/thing1.pem
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/mail/test/server.pem
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/test/server.pem
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/internet/test/fake_CAs/chain.pem
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/internet/test/fake_CAs/thing2.pem
%{__rm} -v $RPM_BUILD_ROOT%{py_sitedir}/twisted/internet/test/fake_CAs/thing2-duplicate.pem

# non-executable-script
#%{__chmod} +x $RPM_BUILD_ROOT%{py_sitedir}/twisted/mail/test/pop3testserver.py
%{__chmod} +x $RPM_BUILD_ROOT%{py_sitedir}/twisted/python/test/pullpipe.py
%{__chmod} +x $RPM_BUILD_ROOT%{py_sitedir}/twisted/trial/test/scripttest.py

# non-standard-executable-perm
%{__chmod} 755 $RPM_BUILD_ROOT%{py_sitedir}/twisted/python/sendmsg.so
%{__chmod} 755 $RPM_BUILD_ROOT%{py_sitedir}/twisted/runner/portmap.so
%{__chmod} 755 $RPM_BUILD_ROOT%{py_sitedir}/twisted/test/raiser.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING LICENSE NEWS README
%attr(755,root,root) %{_bindir}/cftp
%attr(755,root,root) %{_bindir}/ckeygen
%attr(755,root,root) %{_bindir}/conch
%attr(755,root,root) %{_bindir}/lore
%attr(755,root,root) %{_bindir}/mailmail
%attr(755,root,root) %{_bindir}/manhole
%attr(755,root,root) %{_bindir}/pyhtmlizer
%attr(755,root,root) %{_bindir}/tap2deb
%attr(755,root,root) %{_bindir}/tap2rpm
%attr(755,root,root) %{_bindir}/tapconvert
%attr(755,root,root) %{_bindir}/tkconch
%attr(755,root,root) %{_bindir}/trial
%attr(755,root,root) %{_bindir}/twistd
%{_mandir}/man1/cftp.1*
%{_mandir}/man1/ckeygen.1*
%{_mandir}/man1/conch.1*
%{_mandir}/man1/lore.1*
%{_mandir}/man1/mailmail.1*
%{_mandir}/man1/manhole.1*
%{_mandir}/man1/pyhtmlizer.1*
%{_mandir}/man1/tap2deb.1*
%{_mandir}/man1/tap2rpm.1*
%{_mandir}/man1/tapconvert.1*
%{_mandir}/man1/tkconch.1*
%{_mandir}/man1/trial.1*
%{_mandir}/man1/twistd.1*
%{py_sitedir}/twisted
%{py_sitedir}/Twisted-%{version}-py*.egg-info
