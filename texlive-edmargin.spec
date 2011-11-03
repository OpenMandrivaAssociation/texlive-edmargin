# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/edmargin
# catalog-date 2008-08-19 08:58:40 +0200
# catalog-license lppl
# catalog-version 1.02
Name:		texlive-edmargin
Version:	1.02
Release:	1
Summary:	Multiple series of endnotes for critical editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/edmargin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Edmargin provides a very simple scheme for endnote sections for
critical editions. Endnotes can either be marked in the text,
or with marginal references to the page in the note sections
where the note is to be found. Notes can be set in individual
paragraphs, or in block paragraph mode (where there are many
short notes). Note sections will have running headers of the
form "Textual notes to pp. xx--yy". New note sections can be
created on the fly. There are predefined endnote sections for
textual notes, emendations, and explanatory notes.

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
%{_texmfdistdir}/tex/latex/edmargin/edmargin.sty
%doc %{_texmfdistdir}/doc/latex/edmargin/README
%doc %{_texmfdistdir}/doc/latex/edmargin/edmargin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/edmargin/edmargin.dtx
%doc %{_texmfdistdir}/source/latex/edmargin/edmargin.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
