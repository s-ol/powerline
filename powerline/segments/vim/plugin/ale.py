# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)

try:
	import vim
except ImportError:
	vim = object()

from powerline.segments.vim import window_cached
from powerline.bindings.vim import vim_global_exists


@window_cached
def num_warnings(pl, err_format='{num} ERR', warn_format='{num} WARN'):
	'''Show whether ale has found any errors or warnings

	:param str err_format:
			Format string for errors.

	:param str warn_format:
			Format string for warnings.

	Highlight groups used: ``ale:warning`` or ``warning``, ``ale:error`` or ``error``.
	'''

	getWarningCount = vim.Function('ale#statusline#Count')
	res = getWarningCount(vim.current.buffer.number)

	if isinstance(res, vim.List):
		(errors, warnings) = res
		segments = []
		if errors > 0:
			segments.append({
				'contents': err_format.format(num=errors),
				'highlight_groups': ['ale:error', 'error'],
			})
		if warnings > 0:
			segments.append({
			'contents': warn_format.format(num=warnings),
			'highlight_groups': ['ale:warning', 'warning'],
			})
		return segments
