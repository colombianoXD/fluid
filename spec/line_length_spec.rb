# spec/overcommit/pre_commit/line_length_spec.rb

require 'spec_helper'
require 'overcommit'
require 'overcommit/hook/pre_commit/base'
require Rails.root.join('.git-hooks/pre_commit/line_length')

describe Overcommit::Hook::PreCommit::LineLength do
  let(:config) do
    # Load our settings file and initialize an instance of `Overcommit::Configuration`.
    Overcommit::Configuration.new(YAML.load_file('.overcommit.yml'))
  end

  # The context which the hook is running in. For pre-commit hooks, it will be
  # an instance of `Overcommit::HookContext::Precommit`. However, we would not be
  # needing this in our tests so we will just create a double for it.
  let(:context) { double('context') }

  # Path to our fixture.
  let(:staged_file) { '<your_app>/spec/overcommit/fixtures/test_file.txt' }

  # Create an instance of our hook passing in our configuration and context.
  subject! { described_class.new(config, context) }

  before do
    # Stub `applicable_files` to return our fixture.
    allow(subject).to receive(:applicable_files).and_return([staged_file])
  end

  context 'when file contains line which are too long' do
    context 'when all the lines have been modified' do
      before do
        # Stub `modified_lines` to return the scenario where all 3 lines have been
        # modified.
        allow(subject).to receive(:modified_lines).and_return([1, 2, 3])
      end

      it 'should return the right status and error message' do
        expect(subject.run).to eq(
          [
            :fail,
            "#{staged_file}:1: Line is too long [99/89]\n" <<
            "#{staged_file}:3: Line is too long [99/89]"
          ]
        )
      end
    end

    context 'when only the second line has been modified' do
      # Assert that `subject.run` to return `:warn` with our warning lines.
    end
  end

  context 'when file do not contain line which are too long' do
    # Assert that `subject.run` to return `:pass`
  end
end
