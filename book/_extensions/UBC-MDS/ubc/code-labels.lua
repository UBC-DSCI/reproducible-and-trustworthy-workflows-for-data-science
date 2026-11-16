--- Default labels for static listings.
---
--- Every listing in the book says where its contents belong: a `bash` block is
--- something you type in the Terminal, an `out` block is the machine answering
--- back. Those two labels never vary, so writing `filename="Terminal"` on all
--- ~150 of them would be noise that decays the first time someone forgets.
--- This filter supplies them, leaving `filename` free to say something more
--- useful when there is something more useful to say:
---
---     ```bash                              -> labelled "Terminal"
---     ```out                               -> labelled "Output"
---     ```{.bash filename="Terminal (~/)"}  -> left alone, keeps its own label
---     ```python                            -> left alone, no default
---
--- `python` and `r` deliberately have no default. Their context genuinely
--- varies -- `install.packages()` goes in the R console, `penguins.py` is a
--- file on disk -- so those blocks carry an explicit `filename`, and a missing
--- one is caught by `scripts/check_css.py`.
---
--- Why this builds the wrapper by hand rather than just setting the attribute:
--- Quarto turns `filename` into its header bar earlier than any user filter can
--- run, so a `filename` set here would reach the page as a bare `data-filename`
--- attribute and never grow a bar. Emitting the same markup Quarto does means
--- an automatic label and a hand-written one are the same thing by the time the
--- HTML is written, and `styles.scss` only has to style one construct.

local DEFAULT_LABEL = {
  bash = "Terminal",
  out = "Output",
}

local function escape(text)
  return text:gsub("&", "&amp;"):gsub("<", "&lt;"):gsub(">", "&gt;")
end

function CodeBlock(block)
  -- An explicit `filename` wins; Quarto has already drawn its bar.
  if block.attributes["filename"] then
    return nil
  end

  -- Executed cells are left alone. Quarto wraps a cell and its output together
  -- in a `.cell` div, which already pairs them visually, and only the code half
  -- would be reachable from here -- labelling it would leave the output half
  -- unlabelled and imply a distinction that isn't there.
  if block.classes:includes("cell-code") then
    return nil
  end

  for _, class in ipairs(block.classes) do
    local label = DEFAULT_LABEL[class]
    if label then
      local header = pandoc.RawBlock(
        "html",
        '<div class="code-with-filename-file"><pre><strong>'
          .. escape(label)
          .. "</strong></pre></div>"
      )
      return pandoc.Div({ header, block }, pandoc.Attr("", { "code-with-filename" }))
    end
  end
end
