# revision 19440
# category Package
# catalog-ctan /macros/latex/contrib/flacards
# catalog-date 2010-01-16 19:56:06 +0100
# catalog-license gpl
# catalog-version 0.1.1b
Name:		texlive-flacards
Version:	0.1.1b
Release:	1
Summary:	Generate flashcards for printing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/flacards
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flacards.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/flacards.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The flacards class provides an easy interface to produce
flashcards. It will print several cards per page, on both sides
of the paper.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
