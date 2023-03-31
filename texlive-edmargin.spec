Name:		texlive-edmargin
Version:	27599
Release:	2
Summary:	Multiple series of endnotes for critical editions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/edmargin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/edmargin/edmargin.sty
%doc %{_texmfdistdir}/doc/latex/edmargin/README
%doc %{_texmfdistdir}/doc/latex/edmargin/edmargin.pdf
#- source
%doc %{_texmfdistdir}/source/latex/edmargin/edmargin.dtx
%doc %{_texmfdistdir}/source/latex/edmargin/edmargin.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
