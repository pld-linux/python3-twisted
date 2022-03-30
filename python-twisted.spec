# TODO
# - split back to subpackages (python-tkinter, etc deps)
# - package zsh completion
#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (some failures)

Summary:	Twisted - a networking engine written in Python
Summary(pl.UTF-8):	Twisted - silnik sieciowy napisany w Pythonie
Name:		python-twisted
Version:	20.3.0
Release:	5
License:	MIT
Group:		Libraries/Python
Source0:	http://twistedmatrix.com/Releases/Twisted/20.3/Twisted-%{version}.tar.bz2
# Source0-md5:	fc16d575730db7d0cddd09fc35af3eea
URL:		http://twistedmatrix.com/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-incremental >= 16.10.1
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-attrs >= 19.2.0
BuildRequires:	python-automat >= 0.3.0
BuildRequires:	python-constantly >= 15.1
BuildRequires:	python-hyperlink >= 17.1.1
BuildRequires:	python-pyhamcrest >= 1.9.0
BuildRequires:	python-zope.interface >= 4.4.2
# conch
BuildRequires:	python-appdirs >= 1.4.0
BuildRequires:	python-bcrypt >= 3.0.0
BuildRequires:	python-cryptography >= 2.5
BuildRequires:	python-pyasn1
# http2
BuildRequires:	python-h2 >= 3.0
BuildRequires:	python-h2 < 4.0
BuildRequires:	python-priority >= 1.1.0
BuildRequires:	python-priority < 2.0
# serial
BuildRequires:	python-serial >= 3.0
# soappy (python 2 only)
BuildRequires:	python-SOAP
# tls
BuildRequires:	python-idna >= 2.4
BuildRequires:	python-pyOpenSSL >= 16.0.0
BuildRequires:	python-service_identity >= 18.1.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-incremental >= 16.10.1
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-attrs >= 19.2.0
BuildRequires:	python3-automat >= 0.3.0
BuildRequires:	python3-constantly >= 15.1
BuildRequires:	python3-hyperlink >= 17.1.1
BuildRequires:	python3-pyhamcrest >= 1.9.0
BuildRequires:	python3-zope.interface >= 4.4.2
# conch
BuildRequires:	python3-appdirs >= 1.4.0
BuildRequires:	python3-bcrypt >= 3.0.0
BuildRequires:	python3-cryptography >= 2.5
BuildRequires:	python3-pyasn1
# http2
BuildRequires:	python3-h2 >= 3.0
BuildRequires:	python3-h2 < 4.0
BuildRequires:	python3-priority >= 1.1.0
BuildRequires:	python3-priority < 2.0
# serial
BuildRequires:	python3-serial >= 3.0
# tls
BuildRequires:	python3-idna >= 2.4
BuildRequires:	python3-pyOpenSSL >= 16.0.0
BuildRequires:	python3-service_identity >= 18.1.0
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sphinx-pdg >= 1.3.1
Requires:	python-pyOpenSSL >= 0.10
Requires:	python-zope.interface >= 3.6.0
# python-TwistedConch
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

%description -l pl.UTF-8
Twisted to napisany w Pythonie silnik sieciowy, obsługujący wiele
protokołów. Zawiera serwer WWW, wiele klientów czatów, serwery czatów,
serwery pocztowe itp.

%package -n python3-twisted
Summary:	Twisted - a networking engine written in Python
Summary(pl.UTF-8):	Twisted - silnik sieciowy napisany w Pythonie
Group:		Libraries/Python

%description -n python3-twisted
Twisted is a networking engine written in Python, supporting numerous
protocols. It contains a web server, numerous chat clients, chat
servers, mail servers and more.

%description -n python3-twisted -l pl.UTF-8
Twisted to napisany w Pythonie silnik sieciowy, obsługujący wiele
protokołów. Zawiera serwer WWW, wiele klientów czatów, serwery czatów,
serwery pocztowe itp.

%package apidocs
Summary:	Documentation for Twisted networking engine
Summary(pl.UTF-8):	Dokumentacja do silnika sieciowego Twisted
Group:		Documentation
BuildArch:	noarch

%description apidocs
Documentation for Twisted networking engine.

%description apidocs -l pl.UTF-8
Dokumentacja do silnika sieciowego Twisted.

%prep
%setup -q -n Twisted-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
PYTHONPATH=$(pwd)/src \
%{__python} -m twisted.trial --reactor=default --reporter=verbose twisted
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m twisted.trial --reactor=default --reporter=verbose twisted
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/twisted/*/test
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/twisted/python/twisted-completion.zsh
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/twisted/test/test_defer.py.3only

%py_postclean

# install man pages
for s in conch core mail; do
	for f in docs/$s/man/*.1 ; do
		cp -p "$f" $RPM_BUILD_ROOT%{_mandir}/man1/$(basename $f .1)-2.1
	done
done

for f in $RPM_BUILD_ROOT%{_bindir}/* ; do
	%{__mv} "$f" "${f}-2"
done
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitedir}/twisted/*/test
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/twisted/python/twisted-completion.zsh
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/twisted/test/test_defer.py.3only

# install man pages
for s in conch core mail; do
	for f in docs/$s/man/*.1 ; do
		cp -p "$f" $RPM_BUILD_ROOT%{_mandir}/man1/$(basename $f .1)-3.1
	done
done

for f in $RPM_BUILD_ROOT%{_bindir}/* ; do
	[ "${f%%-2}" != "$f" ] || %{__mv} "$f" "${f}-3"
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/cftp-2
%attr(755,root,root) %{_bindir}/ckeygen-2
%attr(755,root,root) %{_bindir}/conch-2
%attr(755,root,root) %{_bindir}/mailmail-2
%attr(755,root,root) %{_bindir}/pyhtmlizer-2
%attr(755,root,root) %{_bindir}/tkconch-2
%attr(755,root,root) %{_bindir}/trial-2
%attr(755,root,root) %{_bindir}/twist-2
%attr(755,root,root) %{_bindir}/twistd-2
%dir %{py_sitedir}/twisted
%{py_sitedir}/twisted/_threads
%{py_sitedir}/twisted/application
%{py_sitedir}/twisted/conch
%{py_sitedir}/twisted/cred
%{py_sitedir}/twisted/enterprise
%{py_sitedir}/twisted/internet
%{py_sitedir}/twisted/logger
%{py_sitedir}/twisted/mail
%{py_sitedir}/twisted/names
%{py_sitedir}/twisted/news
%{py_sitedir}/twisted/pair
%{py_sitedir}/twisted/persisted
%{py_sitedir}/twisted/plugins
%{py_sitedir}/twisted/positioning
%{py_sitedir}/twisted/protocols
%dir %{py_sitedir}/twisted/python
%{py_sitedir}/twisted/python/_pydoctortemplates
%attr(755,root,root) %{py_sitedir}/twisted/python/_sendmsg.so
%{py_sitedir}/twisted/python/*.py[co]
%{py_sitedir}/twisted/runner
%{py_sitedir}/twisted/scripts
%{py_sitedir}/twisted/spread
%{py_sitedir}/twisted/tap
%dir %{py_sitedir}/twisted/test
%attr(755,root,root) %{py_sitedir}/twisted/test/raiser.so
%{py_sitedir}/twisted/test/*.py[co]
%{py_sitedir}/twisted/test/*.pem*
%{py_sitedir}/twisted/trial
%{py_sitedir}/twisted/web
%{py_sitedir}/twisted/words
%{py_sitedir}/twisted/*.py[co]
%{py_sitedir}/Twisted-%{version}-py*.egg-info
%{_mandir}/man1/cftp-2.1*
%{_mandir}/man1/ckeygen-2.1*
%{_mandir}/man1/conch-2.1*
%{_mandir}/man1/mailmail-2.1*
%{_mandir}/man1/pyhtmlizer-2.1*
%{_mandir}/man1/tkconch-2.1*
%{_mandir}/man1/trial-2.1*
%{_mandir}/man1/twistd-2.1*
%endif

%if %{with python3}
%files -n python3-twisted
%defattr(644,root,root,755)
%doc LICENSE NEWS.rst README.rst
%attr(755,root,root) %{_bindir}/cftp-3
%attr(755,root,root) %{_bindir}/ckeygen-3
%attr(755,root,root) %{_bindir}/conch-3
%attr(755,root,root) %{_bindir}/mailmail-3
%attr(755,root,root) %{_bindir}/pyhtmlizer-3
%attr(755,root,root) %{_bindir}/tkconch-3
%attr(755,root,root) %{_bindir}/trial-3
%attr(755,root,root) %{_bindir}/twist-3
%attr(755,root,root) %{_bindir}/twistd-3
%dir %{py3_sitedir}/twisted
%{py3_sitedir}/twisted/__pycache__
%{py3_sitedir}/twisted/_threads
%{py3_sitedir}/twisted/application
%{py3_sitedir}/twisted/conch
%{py3_sitedir}/twisted/cred
%{py3_sitedir}/twisted/enterprise
%{py3_sitedir}/twisted/internet
%{py3_sitedir}/twisted/logger
%{py3_sitedir}/twisted/mail
%{py3_sitedir}/twisted/names
%{py3_sitedir}/twisted/pair
%{py3_sitedir}/twisted/persisted
%{py3_sitedir}/twisted/plugins
%{py3_sitedir}/twisted/positioning
%{py3_sitedir}/twisted/protocols
%dir %{py3_sitedir}/twisted/python
%{py3_sitedir}/twisted/python/__pycache__
%{py3_sitedir}/twisted/python/_pydoctortemplates
%{py3_sitedir}/twisted/python/*.py
%{py3_sitedir}/twisted/runner
%{py3_sitedir}/twisted/scripts
%{py3_sitedir}/twisted/spread
%{py3_sitedir}/twisted/tap
%dir %{py3_sitedir}/twisted/test
%{py3_sitedir}/twisted/test/__pycache__
%attr(755,root,root) %{py3_sitedir}/twisted/test/raiser.cpython-*.so
%{py3_sitedir}/twisted/test/*.py
%{py3_sitedir}/twisted/test/*.pem*
%{py3_sitedir}/twisted/trial
%{py3_sitedir}/twisted/web
%{py3_sitedir}/twisted/words
%{py3_sitedir}/twisted/*.py
%{py3_sitedir}/Twisted-%{version}-py*.egg-info
%{_mandir}/man1/cftp-3.1*
%{_mandir}/man1/ckeygen-3.1*
%{_mandir}/man1/conch-3.1*
%{_mandir}/man1/mailmail-3.1*
%{_mandir}/man1/pyhtmlizer-3.1*
%{_mandir}/man1/tkconch-3.1*
%{_mandir}/man1/trial-3.1*
%{_mandir}/man1/twistd-3.1*
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_downloads,_images,_static,conch,core,historic,installation,mail,names,pair,web,words,*.html,*.js}
%endif
