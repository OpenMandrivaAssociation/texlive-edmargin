%global tl_name edmargin
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Multiple series of endnotes for critical editions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/edmargin
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/edmargin.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Edmargin provides a very simple scheme for endnote sections for critical
editions. Endnotes can either be marked in the text, or with marginal
references to the page in the note sections where the note is to be
found. Notes can be set in individual paragraphs, or in block paragraph
mode (where there are many short notes). Note sections will have running
headers of the form "Textual notes to pp. xx--yy". New note sections can
be created on the fly. There are predefined endnote sections for textual
notes, emendations, and explanatory notes.

