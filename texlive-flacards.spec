%global tl_name flacards
%global tl_revision 19440

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1.1b
Release:	%{tl_revision}.1
Summary:	Generate flashcards for printing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/flacards
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flacards.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/flacards.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The flacards class provides an easy interface to produce flashcards. It
will print several cards per page, on both sides of the paper.

