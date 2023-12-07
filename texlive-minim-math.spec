Name:		texlive-minim-math
Version:	68612
Release:	1
Summary:	Extensive maths for LuaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/minim-math
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-math.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/minim-math.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a simple and highly configurable way to
use Unicode and OpenType mathematics with simple LuaTeX, taking
advantage of most of the engine's new capabilities in
mathematical typesetting. Also included are the proper settings
and definitions for almost all Unicode mathematical characters.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/minim-math
%doc %{_texmfdistdir}/doc/luatex/minim-math

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
