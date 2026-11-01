-- The dependency path carries the extension version, so a new release gets a
-- new URL and browsers/CDNs never serve a stale bundle.
local function extension_version()
  local path = quarto.utils.resolve_path('_extension.yml')
  local f = assert(io.open(path, 'r'), 'quizdown: cannot read ' .. path)
  local yml = f:read('*a')
  f:close()
  return assert(yml:match('version:%s*([%w%.%-]+)'), 'quizdown: no version in _extension.yml')
end

local function ensureHtmlDeps()
  quarto.doc.add_html_dependency({
    name = 'quizdown',
    version = extension_version(),
    scripts = {
      'assets/quizdown.js',
      'assets/quizdownKatex.js',
      'assets/quizdownHighlight.js',
      'assets/quizdown-init.js'
    }
  })
end

-- The page must receive quiz text as text: quizdown.js reads the div's
-- innerHTML and decodes these three entities before parsing (parser.ts htmlDecode).
local function escape_html(s)
  s = s:gsub('&', '&amp;')
  s = s:gsub('<', '&lt;')
  s = s:gsub('>', '&gt;')
  return s
end

function CodeBlock(block)
  if block.classes:includes('{quizdown}') or block.classes:includes('quizdown') then
    ensureHtmlDeps()
    return pandoc.RawBlock('html', '<div class="quizdown">\n' .. escape_html(block.text) .. '\n</div>')
  end
end

-- Also on pages without a quizdown block, for hand-written <div class="quizdown">.
if quarto.doc.is_format("html:js") then
  ensureHtmlDeps()
end
