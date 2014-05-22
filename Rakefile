require 'rake/clean'

LIB_NAME           = 'VUA_pylib'
UPSTREAM_DIRECTORY = "upstream/#{LIB_NAME}-master"

CLEAN.include('upstream', 'build', 'dist', 'MANIFEST')

directory 'upstream' do |task|
  sh "wget https://github.com/cltl/#{LIB_NAME}/archive/master.zip"
  sh "unzip master.zip -d #{task.name}"
  sh 'rm master.zip'
end

directory 'test_scripts' do |task|
  sh "rm -rf #{task.name}"
  sh "mv #{UPSTREAM_DIRECTORY}/#{task.name} #{task.name}"
end

directory LIB_NAME do |task|
  sh "rm -rf #{LIB_NAME}"
  sh "mv #{UPSTREAM_DIRECTORY} #{task.name}"
end

file 'README.md' do |task|
  sh "mv #{UPSTREAM_DIRECTORY}/#{task.name} #{task.name}"
end

file '.gitignore' do |task|
  sh "mv #{UPSTREAM_DIRECTORY}/#{task.name} #{task.name}"
end

desc 'Syncs with the upstream package'
task :sync => [
  'upstream',
  'test_scripts',
  'README.md',
  '.gitignore',
  LIB_NAME,
  'clean'
]

desc 'Builds the Python package'
task :package do
  sh 'python setup.py sdist'
end
