# TODO
# - complete docs and tests (missing BRs)
# - split back to subpackages (python-tkinter, etc deps)
# - package zsh completion
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (some failures)

Summary:	Twisted - a networking engine written in Python
Summary(pl.UTF-8):	Twisted - silnik sieciowy napisany w Pythonie
Name:		python3-twisted
Version:	25.5.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/Twisted/
Source0:	https://files.pythonhosted.org/packages/source/t/twisted/twisted-%{version}.tar.gz
# Source0-md5:	845d6782c2236ef764f3849948f4bfad
Source1:	https://raw.githubusercontent.com/twisted/twisted/refs/tags/twisted-%{version}/setup.cfg
# Source1-md5:	7853a82dfd42b7c399c7d9327b7f4279
URL:		https://twistedmatrix.com/
BuildRequires:	python3-build
BuildRequires:	python3-hatchling >= 1.10.0
BuildRequires:	python3-hatch-fancy-pypi-readme >= 22.5.0
BuildRequires:	python3-incremental >= 24.7.0
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
%if %{with tests}
BuildRequires:	python3-attrs >= 19.2.0
BuildRequires:	python3-automat >= 0.8.0
BuildRequires:	python3-constantly >= 15.1
# TODO
BuildRequires:	python3-cython-test-exception-raiser >= 1.0.2
BuildRequires:	python3-cython-test-exception-raiser < 2
BuildRequires:	python3-hyperlink >= 17.1.1
BuildRequires:	python3-pyhamcrest >= 1.9.0
BuildRequires:	python3-zope.interface >= 4.4.2
# conch
BuildRequires:	python3-appdirs >= 1.4.0
BuildRequires:	python3-bcrypt >= 3.0.0
BuildRequires:	python3-cryptography >= 2.6
BuildRequires:	python3-pyasn1
# conch_nacl
BuildRequires:	python3-PyNaCl
# http2
BuildRequires:	python3-h2 >= 3.0
BuildRequires:	python3-h2 < 5.0
BuildRequires:	python3-priority >= 1.1.0
BuildRequires:	python3-priority < 2.0
# serial
BuildRequires:	python3-serial >= 3.0
# tls
BuildRequires:	python3-idna >= 2.4
BuildRequires:	python3-pyOpenSSL >= 16.0.0
BuildRequires:	python3-service_identity >= 18.1.0
%endif
BuildRequires:	rpmbuild(macros) >= 2.044
%if %{with doc}
# TODO
BuildRequires:	python3-pydoctor >= 21.9.0
BuildRequires:	python3-sphinx_rtd_theme >= 0.5
BuildRequires:	python3-readthedocs-sphinx-ext >= 2.1
BuildRequires:	sphinx-pdg >= 4.1.2
%endif
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted is a networking engine written in Python, supporting numerous
protocols. It contains a web server, numerous chat clients, chat
servers, mail servers and more.

%description -l pl.UTF-8
Twisted to napisany w Pythonie silnik sieciowy, obsługujący wiele
protokołów. Zawiera serwer WWW, wiele klientów czatów, serwery czatów,
serwery pocztowe itp.

%package apidocs
Summary:	Documentation for Twisted networking engine
Summary(pl.UTF-8):	Dokumentacja do silnika sieciowego Twisted
Group:		Documentation

%description apidocs
Documentation for Twisted networking engine.

%description apidocs -l pl.UTF-8
Dokumentacja do silnika sieciowego Twisted.

%prep
%setup -q -n twisted-%{version}

cp -p %{SOURCE1} .

%{__sed} -i -e '/^_git_reference =/,/^)/ c _git_reference="%{version}"' docs/conf.py

%build
%py3_build_pyproject

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -m twisted.trial --reactor=default --reporter=verbose twisted
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C docs html
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%py3_install_pyproject

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/twisted/*/test
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/twisted/python/twisted-completion.zsh

# install man pages
for s in conch core mail; do
	for f in docs/$s/man/*.1 ; do
		cp -p "$f" $RPM_BUILD_ROOT%{_mandir}/man1/$(basename $f .1)-3.1
	done
done

for f in $RPM_BUILD_ROOT%{_bindir}/* ; do
	[ "${f%%-2}" != "$f" ] || %{__mv} "$f" "${f}-3"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
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
%{py3_sitescriptdir}/twisted
%{py3_sitescriptdir}/twisted-%{version}.dist-info
%{_mandir}/man1/cftp-3.1*
%{_mandir}/man1/ckeygen-3.1*
%{_mandir}/man1/conch-3.1*
%{_mandir}/man1/mailmail-3.1*
%{_mandir}/man1/pyhtmlizer-3.1*
%{_mandir}/man1/tkconch-3.1*
%{_mandir}/man1/trial-3.1*
%{_mandir}/man1/twistd-3.1*

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_downloads,_images,_static,conch,core,historic,installation,mail,names,pair,web,words,*.html,*.js}
%endif
