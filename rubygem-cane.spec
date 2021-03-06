#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-cane
Version  : 3.0.0
Release  : 10
URL      : https://rubygems.org/downloads/cane-3.0.0.gem
Source0  : https://rubygems.org/downloads/cane-3.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: rubygem-cane-bin
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-docile
BuildRequires : rubygem-parallel
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-fire
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html

%description
# Cane
Fails your build if code quality thresholds are not met.
> Discipline will set you free.

%package bin
Summary: bin components for the rubygem-cane package.
Group: Binaries

%description bin
bin components for the rubygem-cane package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n cane-3.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-cane.gemspec

%build
export LANG=C
gem build rubygem-cane.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
cane-3.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/cane-3.0.0
rspec -I.:lib spec/ || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/cane-3.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/HISTORY.md
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/bin/cane
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/cane.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/.last_run.json
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/.resultset.json
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/.resultset.json.lock
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/application.css
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/application.js
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/colorbox/border.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/colorbox/controls.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/colorbox/loading.gif
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/colorbox/loading_background.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/favicon_green.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/favicon_red.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/favicon_yellow.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/loading.gif
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/magnify.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-bg_flat_0_aaaaaa_40x100.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-bg_flat_75_ffffff_40x100.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_55_fbf9ee_1x400.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_65_ffffff_1x400.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_75_dadada_1x400.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_75_e6e6e6_1x400.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-bg_glass_95_fef1ec_1x400.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-bg_highlight-soft_75_cccccc_1x100.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-icons_222222_256x240.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-icons_2e83ff_256x240.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-icons_454545_256x240.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-icons_888888_256x240.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/assets/0.10.0/smoothness/images/ui-icons_cd0a0a_256x240.png
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/covered_percent
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/coverage/index.html
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/abc_check.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/cli.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/cli/options.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/cli/parser.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/default_checks.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/doc_check.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/encoding_aware_iterator.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/file.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/json_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/rake_task.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/style_check.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/task_runner.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/threshold_check.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/lib/cane/violation_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/abc_check_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/cane_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/cli_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/doc_check_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/encoding_aware_iterator_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/file_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/fixtures/a/1.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/fixtures/b/1.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/json_formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/parser_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/rake_task_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/runner_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/style_check_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/threshold_check_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/cane-3.0.0/spec/violation_formatter_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/cane-3.0.0.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/cane
