# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/flacards
# catalog-date 2010-01-16 19:56:06 +0100
# catalog-license gpl
# catalog-version 0.1.1b
Name:		texlive-flacards
Version:	0.1.1b
Release:	8
Summary:	Generate flashcards for printing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flacards
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flacards.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flacards.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1b-2
+ Revision: 751920
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1.1b-1
+ Revision: 718456
- texlive-flacards
- texlive-flacards
- texlive-flacards
- texlive-flacards

