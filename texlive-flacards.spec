Name:		texlive-flacards
Version:	19440
Release:	2
Summary:	Generate flashcards for printing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/flacards
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flacards.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flacards.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The flacards class provides an easy interface to produce
flashcards. It will print several cards per page, on both sides
of the paper.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/flacards/flacards.cls
%doc %{_texmfdistdir}/doc/latex/flacards/COPYING
%doc %{_texmfdistdir}/doc/latex/flacards/README
%doc %{_texmfdistdir}/doc/latex/flacards/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/flacards/changelog.txt
%doc %{_texmfdistdir}/doc/latex/flacards/flacards_ex.pdf
%doc %{_texmfdistdir}/doc/latex/flacards/flacards_ex.tex
%doc %{_texmfdistdir}/doc/latex/flacards/flacards_ex1.tex
%doc %{_texmfdistdir}/doc/latex/flacards/flacards_ex2.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
